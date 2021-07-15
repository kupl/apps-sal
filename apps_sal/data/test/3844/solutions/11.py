from collections import Counter

n = int(input())
a = [int(v) for v in input().split()]

cnt = Counter(a)

print('Agasa' if all(v % 2 == 0 for v in list(cnt.values())) else 'Conan')

