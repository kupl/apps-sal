class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]

        mydictionary = defaultdict(set)
        mydictionaryextra = defaultdict(set)
        for number in A:
            value = number
            for prime in primes:
                if prime > value:
                    break
                if value % prime == 0:
                    while value % prime == 0:
                        value = value // prime
                    mydictionary[prime].add(number)
            if 50000 > value > 1:
                mydictionaryextra[value].add(number)

        for key, value in mydictionaryextra.items():
            if len(value) > 1:
                mydictionary[key] = value

        maximum = 1

        while mydictionary:
            component = mydictionary.pop(next(iter(mydictionary.keys())))
            flag = True
            while flag:
                flag = False
                primes = list(mydictionary.keys())
                for prime in primes:
                    if prime in mydictionary and component.intersection(mydictionary[prime]):
                        flag = True
                        component.update(mydictionary.pop(prime))
            maximum = max(maximum, len(component))

        return maximum
