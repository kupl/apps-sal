a = input()
if a.startswith("CODEFORCES") or a.endswith("CODEFORCES"):
    print("YES")
    return
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[:i]+a[j+1:]=="CODEFORCES":
            print("YES")
            return
print("NO")
