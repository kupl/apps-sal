# APPS dataset refined by SAL
APPS is a python coding competition dataset.
The original contents can be found in [here](https://github.com/hendrycks/apps).

## Refined
We (SAL, Software Analysis Laboratory) refined the original dataset.

## Installation
You can install `apps-sal` using `pip3`.

### Requirement
`apps-sal` requires python 3.7 or higher.

### Installation
You can install `apps-sal` using `pip` and `git`.

#### Latest Released Version
Currently, the latest released version is `v0.1.0`.
If you set ssh authentication with GitHub, you can install `apps-sal` by simply typing a following command:
```bash
$ [sudo] pip3 install git+https://github.com/kupl/apps-sal.git@v0.1.0
```

### Examples
You can load APPS train set with the following codes:
```python
import apps_sal

train = apps_sal.load_train_dataset()
```

### Changelog
Changes in this project are documented in [CHANGELOG.md](CHANGELOG.md).
