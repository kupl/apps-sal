n = int(input())
ans = 0
dec = 1
while(n >= dec):
    n -= dec
    ans += 1
    dec += ans + 1
print(ans)
