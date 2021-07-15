h, w = (int(x) for x in input().split())
s = []
ans = []
rev = ""
for row in range(1, h+1):
    for col, t in enumerate(input()):
        s.append([(row,col+1),t])

for index, factor in enumerate(s):
    count =0
    if factor[1] != "#":
        if w == 1:
            for point in [index-1, index+1]:
                if 0 <= point and point < len(s) and s[point][1] == "#":
                    count += 1
        elif (index+1)%w == 1:
            for point in [index +1,index -w+1, index -w, index +w, index +w+1]:
                if 0 <= point and point < len(s) and s[point][1] == "#":
                    count += 1
        elif (index+1)%w == 0:
            for point in [index -1,index -w, index -w-1, index +w-1, index +w]:
                if 0 <= point and point < len(s) and s[point][1] == "#":
                    count += 1
        else:
            for point in [index -1, index +1,index -w+1, index -w, index -w-1, index +w-1, index +w, index +w+1]:
                if 0 <= point and point < len(s) and s[point][1] == "#":
                    count += 1
        ans.append(count)
    else:
        ans.append("#")

while(ans != []):
    for num in range(w):
        rev += str(ans[0])
        del ans[0]
    rev += "\n"

print(rev)
