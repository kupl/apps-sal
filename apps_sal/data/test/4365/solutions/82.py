K = int(input())
if K % 2 == 0:
    ans = (K//2)*(K//2)
else:
    K -= 1
    ans = (K//2)*(K//2+1)
print(ans)

