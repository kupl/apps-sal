ans = []
a, b, c = list(map(int, input().split()))

def sumDig(x):
    ret = 0
    if x <= 0:
        return 100500
    while x:
        ret += x % 10
        x //= 10
    return ret 

for s in range(1, 90):
    val = b * pow(s, a) + c
    if 0 < val < 10 ** 9 and sumDig(val) == s:
        ans.append(val)

print(len(ans))
print(' '.join(map(str, sorted(ans))))

