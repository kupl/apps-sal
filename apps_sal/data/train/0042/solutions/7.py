t = int(input())
for _ in [0] * t:
    s = input()
    stack = []
    zero_count = 0
    ans = 0
    for c in map(int, s):
        new_stack = []
        append = new_stack.append
        if c:
            append((c, zero_count))
            ans += 1
            zero_count = 0
        else:
            zero_count += 1
        for (v, zeros) in stack:
            v = (v << 1) + c
            need_zeros = v - v.bit_length()
            if need_zeros <= zeros:
                ans += 1
                append((v, zeros))
        stack = new_stack
    print(ans)
