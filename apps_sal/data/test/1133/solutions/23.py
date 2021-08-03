words = []
n = int(input().strip())
for i in range(n):
    words.append(input().strip())

let = [chr(i) for i in range(ord('a'), ord('z') + 1)]
max_tot_len = 0
for i in range(len(let)):
    for j in range(i + 1, len(let)):
        a = let[i]
        b = let[j]
        tot_len = 0
        for w in words:
            if all([c in [a, b] for c in w]):
                tot_len += len(w)
        if tot_len > max_tot_len:
            max_tot_len = tot_len
print(max_tot_len)
