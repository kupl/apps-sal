with open('input.txt') as fin:
    lines = fin.readlines()
_, k = map(int, lines[0].split())
lights = sorted((int(light), i + 1) for i, light in enumerate(lines[1].split()))
itops = sorted(i for _, i in lights[-k:])
with open('output.txt', 'w') as fout:
    print(lights[-k][0], file=fout)
    print(' '.join(map(str, itops)), file=fout)
