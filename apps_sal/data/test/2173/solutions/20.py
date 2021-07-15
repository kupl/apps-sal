n = int(input());

values = list( map(int, input().split(' ')) );
keys = sorted(list(range(n)), key = lambda a : values[a]);

last = 0;
for a in keys :
    last = max(values[a], last);
    values[a] = last;
    last += 1;

print((*values));

