x = int(input())
p = x//500
ans = 1000*p
x = x%500
p = x//5
ans += p*5
print(ans)
