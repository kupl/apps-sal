from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
m = max(a)
fail = False
for k in c:
    if c[k] % 2 == 1:
        print('Conan')
        fail = True
        break
if not fail:
    print('Agasa')
