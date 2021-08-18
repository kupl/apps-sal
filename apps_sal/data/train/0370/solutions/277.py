
class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def get_primes_set(n):
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return get_primes_set(n // i) | set([i])
            return set([n])

        A = set(A)
        primes = set()

        children_of = collections.defaultdict(set)
        for a in A:
            ap = get_primes_set(a)
            prev = None
            for pr in ap:
                primes.add(pr)
                children_of[pr].add(a)
                if prev is not None:
                    children_of[pr].add(prev)
                    children_of[prev].add(pr)
                prev = pr

        print(children_of)

        seen = set()
        sizes = dict()
        for pr in primes:
            if pr in seen:
                continue
            sizes[pr] = 0
            to_explore = collections.deque([pr])
            while to_explore:
                curr = to_explore.popleft()
                if curr in seen:
                    continue
                seen.add(curr)
                sizes[pr] += curr in A
                for child in children_of[curr]:
                    to_explore.append(child)

        return max(sizes.values())
