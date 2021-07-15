t = int(input())
for _  in range(t):
    w = input()
    h = input()
    works = False
    for i in range(len(h)):
        ls = [h[x] if x < len(h) else "" for x in range(i, i + len(w))]
        if sorted(ls) == sorted(w):
            works = True
            break
    if works:
        print("YES")
    else:
        print("NO")

