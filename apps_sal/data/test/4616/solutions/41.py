s = input()
s_len = len(s)
(head, tail) = (s[0], s[s_len - 1])
print(head + str(s_len - 2) + tail)
