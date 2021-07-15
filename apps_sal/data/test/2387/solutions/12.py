n = int(input())
slist = []
for i in range(n):
    slist.append(input())

first_list = []
last_list = []
first = ""
last = ""
for i in range(n):
    s = slist[i]

    a_count = 0
    b_count = 0
    min_s = ""
    for c in s:
        if c == ")":
            b_count-=1
        else:
            b_count+=1
        if b_count < 0:
            b_count = 0
            a_count+= 1
    min_s = ")"* a_count + "("*b_count

    ai = a_count
    bi = b_count

    if ai == 0:
        first += min_s
    elif bi == 0:
        last += min_s
    elif bi-ai >= 0:
        first_list.append([min_s,ai])
    else:
        last_list.append([min_s,bi])

first_list= sorted(first_list, key=lambda s: s[1])
last_list= sorted(last_list, key=lambda s: s[1], reverse=True)

ans = first
for i in range(len(first_list)):
    ans += first_list[i][0]
for i in range(len(last_list)):
    ans += last_list[i][0]
ans += last

a_count = 0
b_count = 0
min_s = ""
for c in ans:
    if c == ")":
        b_count-=1
    else:
        b_count+=1
    if b_count < 0:
        b_count = 0
        a_count+= 1

if a_count == 0 and b_count == 0:
    print("Yes")
else:
    print("No")
