

src, dest = [int(x) for x in str(input()).strip().split()]
num_steps = 0
if src >= dest:
    num_steps = (src - dest)
else:
    while dest > src:
        if dest % 2 == 1:
            dest += 1
        else:
            dest //= 2
        num_steps += 1
    num_steps += (src - dest)

print(num_steps)
