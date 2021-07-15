n = int(input())
if n&1 and n >= 5:
    print(1, (n-5)//2 + 1)
else:
    print("NO")
