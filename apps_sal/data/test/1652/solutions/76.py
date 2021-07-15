reverse_s = input().strip()[::-1]

while True:
    if len(reverse_s) == 0:
        print("YES")
        return
    if reverse_s.startswith('maerd'):
        reverse_s = reverse_s[len('maerd'):]
    elif reverse_s.startswith('remaerd'):
        reverse_s = reverse_s[len('remaerd'):]
    elif reverse_s.startswith('esare'):
        reverse_s = reverse_s[len('esare'):]
    elif reverse_s.startswith('resare'):
        reverse_s = reverse_s[len('resare'):]
    else:
        print("NO")
        return

