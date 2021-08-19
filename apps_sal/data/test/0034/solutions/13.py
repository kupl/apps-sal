(q, w, e) = list(map(int, input().split()))
s = w + e
tt = s // q
while w // tt + e // tt < q:
    tt -= 1
if tt > min(w, e):
    tt = min(w, e)
print(tt)
