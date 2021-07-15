
n, k = list(map(int, input().split()))
string = input()

res = None
for i in range(1, n):
    if string.startswith(string[i:]):
        res = string[:i] * k + string[i:]
        break

if not res:
    print(string * k)
else:
    print(res)


