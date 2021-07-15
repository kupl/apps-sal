x, y = map(int, input().split())
diff = abs(x - y)
ref = (min(x, y) - diff)//3
total = ref*2 + diff
mod = 10**9 + 7
ans = 1

if (x + y)%3 != 0 or ref < 0:
    print(0)
    return


for i in range(min(ref, total - ref)):
    ans = ans*(total - i)%mod
    ie = pow((i + 1), (mod - 2), mod)
    ans = ans*ie%mod

print(ans)
