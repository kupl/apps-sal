N, H, *blades = map(int, open(0).read().split())
cut = max(blades[::2])
throws = sorted(b for b in blades[1::2] if b >= cut)

ans = 0
while throws:
    H -= throws.pop()
    ans += 1
    if H <= 0:
        print(ans)
        return

ans += (H + cut - 1) // cut
print(ans)
