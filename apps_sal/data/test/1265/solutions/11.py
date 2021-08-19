i = input
(a, b) = (i(), i())
print(['YES', 'NO'][(len(a) != len(b) or set(a) == {'0'} or set(b) == {'0'} or (len(a) < 2)) and a != b])
