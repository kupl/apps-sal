t = int(input())
for _ in range(t):
    s = input()
    cnt1 = 0
    cnt2 = 0
    for i in s:
        if i == '1':
            cnt1+=1
        else:
            cnt2 += 1
    if min(cnt1, cnt2) % 2 == 1:
        print("DA")
    else:
        print("NET")
