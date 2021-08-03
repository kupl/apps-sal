class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def freq(tiles):
            d = {}
            for c in tiles:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
            return d

        def build(d, s):
            new_d = {}
            for key, value in d.items():
                if key == s:
                    new_d[key] = value - 1
                else:
                    new_d[key] = value
            return new_d

        def generate(options):
            sol = []
            for key, value in options.items():
                if value > 0:
                    sol.append(key)
                    fringe = generate(build(options, key))
                    sol += fringe
                    sol += [key + f for f in fringe]
            return sol

        return len(set(generate(freq(tiles))))
