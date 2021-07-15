l = list(map(int, input().split()))
for ll in l:
    if l.count(ll)==1:
        print(ll)
        break
