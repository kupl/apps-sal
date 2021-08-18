class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        divisors, groups, sizes = {}, {}, {}

        for num in A:
            added = False

            for i in range(2, max(int(math.sqrt(num)) + 1, 4)):
                if num % i == 0:
                    added = True

                    if i not in divisors:
                        divisors[i] = set()
                    divisors[i].add(num)

                    if (num_i := int(num / i)) > 1:
                        if num_i not in divisors:
                            divisors[num_i] = set()
                        divisors[num_i].add(num)

            if not added:

                if num not in divisors:
                    divisors[num] = set()
                divisors[num].add(num)

        def union(node1: int, node2: int) -> None:
            parent1 = find(node1)
            parent2 = find(node2)

            if parent1 == parent2:
                return
            elif parent1 < parent2:

                groups[parent2] = parent1
                sizes[parent1] = sizes[parent1] + sizes[parent2]

            else:
                groups[parent1] = parent2
                sizes[parent2] = sizes[parent1] + sizes[parent2]

        def find(node: int) -> int:

            if node not in groups:
                groups[node] = node
                sizes[node] = 1
                return node

            if groups[node] == node:
                return node

            groups[node] = find(groups[node])

            return groups[node]

        for _, common_numbers in list(divisors.items()):
            num1 = random.sample(common_numbers, 1)[0]

            for num2 in common_numbers:
                if num1 != num2:
                    union(num1, num2)

        return max(list(sizes.values()), default=1)
