import re
print('YES' if re.compile(r'^(dream|dreamer|erase|eraser)+$').match(input()) else 'NO')
