n = int(input())
ax, ay = [ int(x) for x in input().split()]
bx, by = [int(x) for x in input().split()]
cx, cy = [int(x) for x in input().split()]

if (bx>ax>cx) or (cx>ax>bx):
        print("NO")
        return
elif (by>ay>cy) or (cy>ay>by):
        print("NO")
        return
print("YES")

