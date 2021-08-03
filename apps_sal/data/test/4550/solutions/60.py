l = list(map(int, input().split()))
print("Yes")if(e := sum(l)) % 2 == 0 and e // 2 in l else print("No")
