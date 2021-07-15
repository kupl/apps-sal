#python3
# utf-8

a, b, f, k = (int(x) for x in input().split())
z = 0

curr_petrol = b
curr_races_made = 0
ans = 0
z___f = f - z
f___a = a - f
if k == 1:
    if z___f > b or f___a > b:
        print(-1)
        return
elif k == 2:
    if 2 * f___a > b:
        print(-1)
        return
else:
    if 2 * z___f > b or 2 * f___a > b:
        print(-1)
        return

#direction, races_made, petrol
curr_save = None
route = [z___f, f___a, f___a, z___f]

while curr_races_made < 2 * k:
    curr_pos = curr_races_made % 4
    curr_petrol -= route[curr_pos]
    curr_races_made += 1
    if curr_petrol < 0:
        curr_petrol = b
        ans += 1
        curr_races_made = curr_save
        continue
    if curr_pos == 0 or curr_pos == 2:
        curr_save = curr_races_made

print(ans)

