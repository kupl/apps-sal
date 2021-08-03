import sys


def input(): return sys.stdin.readline()[:-1]
def print(s): return sys.stdout.write(f"{s}\n")


for _ in range(int(input())):
    sentence = input()
    if sentence.endswith("po"):
        print("FILIPINO")
    elif sentence.endswith("mnida"):
        print("KOREAN")
    else:
        print("JAPANESE")

sys.stdout.flush()
