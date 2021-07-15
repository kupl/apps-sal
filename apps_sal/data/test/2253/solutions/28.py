import sys

input = lambda: sys.stdin.readline()[:-1]
print = lambda s: sys.stdout.write(f"{s}\n")

for _ in range(int(input())):
    sentence = input()
    if sentence.endswith("po"):
        print("FILIPINO")
    elif sentence.endswith("mnida"):
        print("KOREAN")
    else:
        print("JAPANESE")

sys.stdout.flush()

