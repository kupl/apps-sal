(n, m) = map(int, input().split())
in_s = input()
renames_str = [input() for i in range(m)]
rule = {}
rule_inv = {}
for i in range(26):
    c = chr(ord('a') + i)
    rule[c] = c
    rule_inv[c] = c
for x in renames_str:
    (a, b) = x.split()
    for (k, v) in rule.items():
        if v == a:
            rule[k] = b
        if v == b:
            rule[k] = a
for c in in_s:
    print(rule[c], end='')
print()
