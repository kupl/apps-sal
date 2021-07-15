a = input()
b = input()
for i in range(3):
    if a[i] != b[-(i+1)]:
        print("NO")
        break
else:
    print("YES")
