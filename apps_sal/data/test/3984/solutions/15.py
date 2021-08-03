S = input()

max_before = []
smallest_so_far = S[0]

print("Mike")

for s in S[1:]:
    if s > smallest_so_far:
        print("Ann")
    else:
        print("Mike")
    smallest_so_far = min(smallest_so_far, s)
