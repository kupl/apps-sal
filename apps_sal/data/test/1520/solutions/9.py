n = int(input())


# for old string s + t
# find out max length for each character -> inductively
# is t single character
# yes -> longest[char] = (longest[char] + 1) * (len(t) + 1) - 1,
# longest[notchar] = 1 or 0 depending if it existed before
# no -> longest[char] = longest same suffix_t/same prefix_t + 1 / longest[t]
# longest not char = longest[t] or 1 or 0

# need to keep track of
# longest for every character in s
# longest for every character in t
# length of same prefix in t
# length of same suffix in t

def get_longest(s):
    prev_c = -1
    curr_len = 0
    longest = [0] * 26
    for c in s:
        if c != prev_c:
            curr_len = 1
            prev_c = c
        else:
            curr_len += 1
        longest[c] = max(longest[c], curr_len)
    return longest


def get_prefix(s):
    prev_c = s[0]
    curr_len = 0
    for c in s:
        if c == prev_c:
            curr_len += 1
        else:
            return (prev_c, curr_len)
    return (prev_c, curr_len)


def get_suffix(s):
    prev_c = s[len(s)-1]
    curr_len = 0
    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        if c == prev_c:
            curr_len += 1
        else:
            return (prev_c, curr_len)
    return (prev_c, curr_len)


s = [ord(x) - 97 for x in input()]
longest_s = get_longest(s)

for i in range(1, n):
    t = [ord(x) - 97 for x in input()]
    longest_t = get_longest(t)
    prefix = get_prefix(t)
    suffix = get_suffix(t)
    if prefix[1] == len(t):
        for i in range(0, 26):
            if i == t[0]:
                longest_s[i] = (len(t) + 1) * (longest_s[i] + 1) - 1
            else:
                longest_s[i] = int(bool(longest_s[i]))
    else:
        for i in range(0, 26):
            longest_s[i] = int(bool(longest_s[i]))
            if i == prefix[0]:
                longest_s[i] += prefix[1]
            if i == suffix[0]:
                longest_s[i] += suffix[1]
            longest_s[i] = max(longest_s[i], longest_t[i])

print(max(longest_s))

