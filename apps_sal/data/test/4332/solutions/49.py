n = int(input())
s = sum(map(int, list(str(n))))

if n % s == 0:
    print("Yes")
else:
    print("No")
