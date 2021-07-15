s, k = input(), int(input())
if len(s) % k:
    print("NO")
    return

l = int(len(s) / k)
for p in (s[i*l:(i+1)*l] for i in range(k)):
    if p != p[::-1]:
        print("NO")
        return
print("YES")

