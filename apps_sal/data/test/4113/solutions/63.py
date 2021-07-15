n=int(input())
print("Yes" if any((n-4*i)%7==0 for i in range(n//4+1)) else "No")
