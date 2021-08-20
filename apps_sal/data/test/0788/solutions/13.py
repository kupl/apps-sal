import re
print(sum((1 if c == 'A' else int(c) for c in re.findall('10|A|[2-9]', input()))))
