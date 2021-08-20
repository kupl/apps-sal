(k, n) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
all_maybe_all_b = []
for mast_b in b:
    all_maybe_for_b_i = set()
    for slog in a:
        mast_b -= slog
        all_maybe_for_b_i.add(mast_b)
    all_maybe_all_b += [all_maybe_for_b_i]
pack_ans_intersection = set.intersection(*all_maybe_all_b)
print(len(pack_ans_intersection))
