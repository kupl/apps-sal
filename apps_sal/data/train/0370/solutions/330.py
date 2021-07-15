class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        divisors, groups, sizes = {}, {}, {}

        # Find all divisors of the numbers in the list
        for num in A:
            added = False

            for i in range(2, max(int(math.sqrt(num)) + 1, 4)):
                if num % i == 0:
                    added = True

                    # Found two divisors
                    # First is i
                    if i not in divisors:
                        divisors[i] = set()
                    divisors[i].add(num)

                    # Second is num divided by i
                    if (num_i := int(num / i)) > 1:
                        if num_i not in divisors:
                            divisors[num_i] = set()
                        divisors[num_i].add(num)

            if not added:

                # This is a prime number
                if num not in divisors:
                    divisors[num] = set()
                divisors[num].add(num)

        # Union function
        def union(node1: int, node2: int) -> None:
            parent1 = find(node1)
            parent2 = find(node2)

            # Check if these nodes already belong to the same parent
            if parent1 == parent2:
                return
            elif parent1 < parent2:

                # Union to the smallest parent 1
                groups[parent2] = parent1
                sizes[parent1] = sizes[parent1] + sizes[parent2]

            else:
                # Union to the smallest parent 2
                groups[parent1] = parent2
                sizes[parent2] = sizes[parent1] + sizes[parent2]

        # Find function
        def find(node: int) -> int:

            # If this node hasn't been created yet
            if node not in groups:
                groups[node] = node
                sizes[node] = 1
                return node

            # Check if this node is also the parent (final node)
            if groups[node] == node:
                return node

            # Apply path compression
            groups[node] = find(groups[node])

            # Return the parent
            return groups[node]

        # Union-find algorithm to union all groups with common divisor
        for _, common_numbers in list(divisors.items()):
            num1 = random.sample(common_numbers, 1)[0]

            for num2 in common_numbers:
                if num1 != num2:
                    union(num1, num2)

        return max(list(sizes.values()), default=1)

