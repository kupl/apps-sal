n = int(input())
a = ["I hate that", "I love that"]
if n % 2 == 1:
    a.append("I hate it")
else:
    a.append("I love it")
for i in range(n - 1):
    print(a[i % 2], end=" ")
print(a[-1], end="")
