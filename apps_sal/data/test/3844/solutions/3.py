def read():
    return list(map(int, input().split()))


n = int(input())
a = sorted(read())
N = 10 ** 5 + 10
c = [0] * N
for i in a:
    c[i] += 1
ans = 'Agasa'
for i in a:
    if c[i] % 2:
        ans = 'Conan'
print(ans)
