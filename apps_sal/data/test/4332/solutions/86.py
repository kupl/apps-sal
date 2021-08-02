n = int(input())
s = 0
for i in list(str(n)):
    s += int(i)
print("Yes") if n % s == 0 else print("No")
