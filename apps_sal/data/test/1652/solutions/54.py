import re
print('YES' if re.compile('^(dream|dreamer|erase|eraser)+$').match(input()) else 'NO')
