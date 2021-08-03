def string_value(str):
    ans = 0
    valid = True
    neg = False
    after_neg = 0
    for char in str:
        if char == ")":
            ans -= 1
            if after_neg > 0:
                after_neg -= 1
        else:
            ans += 1
            after_neg += 1
        if ans < 0:
            neg = True
    if (after_neg > 0 and neg):
        valid = False
    return valid, ans


num = int(input())
vals = []
for i in range(num):
    valid, ans = string_value(input())
    if valid:
        vals.append(ans)

ans = 0
if len(vals) > 0:
    vals = sorted(vals)
    prev = vals[0]
    occured = 1
    occurances = {}
    keys = []
    for i in vals[1:]:
        if prev != i:
            keys.append(prev)
            occurances[prev] = occured
            occured = 1
            prev = i
        else:
            occured += 1

    occurances[prev] = occured
    keys.append(prev)
    j = 0
    k = len(keys) - 1

    while j <= k:
        if -keys[j] == keys[k]:
            ans += occurances[keys[j]] * occurances[keys[k]]
        if abs(keys[j]) > abs(keys[k]):
            j += 1
        else:
            k -= 1
print(ans)
