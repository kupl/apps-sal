H, W = list(map(int, input().split()))
a_list = [list(input()) for _ in range(H)]
dot_cnt = [sum([a == '.' for a in a_col]) for a_col in a_list]
exist_idx = [i for i, num in enumerate(dot_cnt) if num != W]
st = set(range(W))
for i in exist_idx:
    dot_idx = [i for i, a in enumerate(a_list[i]) if a == '.']
    st = st & set(dot_idx)
for i in exist_idx:
    print((''.join([a for i, a in enumerate(a_list[i]) if i not in st])))

