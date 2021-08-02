import re
import sys

# Lista de Entradas
lst = []
for line in sys.stdin:
    lst.append(line.rstrip("\n"))


regex = [[int(r) for r in re.findall("(\d+)", line)]
         for line in lst]

verifica = lambda x: "Yes" if x % 9 == 0 else "No"

[print(verifica(r[0])) for r in regex]
