n = int(input())
no = set()
mb = set("abcdefghijklmnopqrstuvwxyz")
ans = 0
mark = False
for i in range(n):
    flag, save = input().split()
    if(flag == "!"):
        for_add = set()
        for j in range(len(save)):
            for_add.add(save[j])
        if(len(mb) == 0):
            mb = for_add
        else:
            mb = for_add & mb
        if(mark):
            ans += 1
    elif(flag == "."):
        for j in range(len(save)):
            no.add(save[j])
    else:
        if(i != n - 1):
            no.add(save)
            if(mark):
                ans += 1
    if(len(mb - no) == 1 or len(mb) == 1):
        mark = True

print(ans)
