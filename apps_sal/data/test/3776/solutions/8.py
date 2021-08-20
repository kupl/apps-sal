__author__ = 'Alexander'
import sys
format = int(sys.stdin.readline().strip())
(timeH, timeM) = list(map(int, sys.stdin.readline().split(':')))
if format == 12:
    if timeH > 12 or timeH == 0:
        if timeH == 0:
            timeH = 1
        elif timeH % 10 == 0:
            timeH = 10
        else:
            timeH %= 10
    if timeM > 59:
        timeM %= 10
else:
    if timeH > 23:
        timeH %= 10
    if timeM > 59:
        timeM %= 10
sys.stdout.write('%02d:%02d' % (timeH, timeM))
